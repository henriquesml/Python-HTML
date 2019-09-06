__all__ = ['PyWeb']

import re

class DocError(Exception):
    pass

class PyWeb(object):

    class Tag(object):
        def __init__(self, doc, name, attrs): # name is the tag name (ex: 'div')

            self.doc = doc
            self.name = name
            self.attrs = attrs

        def __enter__(self):
            self.parent_tag = self.doc.current_tag
            self.doc.current_tag = self
            self.position = len(self.doc.result)
            self.doc._append('')

        def __exit__(self, tpe, value, traceback):
            if value is None:
                if self.attrs:
                    self.doc.result[self.position] = "\n<%s %s>\n" % (
                        self.name,
                        dict_to_attrs(self.attrs),
                    )
                else:
                    self.doc.result[self.position] = "<%s>" % self.name
                self.doc._append("\n</%s>" % self.name)
                self.doc.current_tag = self.parent_tag

    class DocumentRoot(object):

        class DocumentRootError(DocError, AttributeError):
            # Raising an AttributeError on __getattr__ instead of just a DocError makes it compatible
            # with the pickle module (some users asked for pickling of SimpleDoc instances).
            # I also keep the DocError from earlier versions to avoid possible compatibility issues
            # with existing code.
            pass

        def __getattr__(self, item):
            raise PyWeb.DocumentRoot.DocumentRootError("DocumentRoot here. You can't access anything here.")

    _newline_rgx = re.compile(r'\r?\n')

    def __init__(self, stag_end = ' />', nl2br = False):
        self.result = []
        self.current_tag = self.__class__.DocumentRoot()
        self._append = self.result.append
        assert stag_end in (' />', '/>', '>')
        self._stag_end = stag_end
        self._br = '<br' + stag_end
        self._nl2br = nl2br

	#aqui entra a tag
    def tag(self, tag_name, *args, **kwargs):

        return self.__class__.Tag(self, tag_name, _attributes(args, kwargs))


    def text(self, *strgs):
        for strg in strgs:
            transformed_string = html_escape(strg)
            if self._nl2br:
                self._append(
                    self.__class__._newline_rgx.sub(
                        self._br,
                        transformed_string
                    )
                )
            else:
                self._append(transformed_string)

    def line(self, tag_name, text_content, *args, **kwargs):
        with self.tag(tag_name, *args, **kwargs):
            self.text(text_content)

    def asis(self, *strgs):
        for strg in strgs:
            if strg is None:
                raise TypeError("Expected a string, got None instead.")
                # passing None by mistake was frequent enough to justify a check
                # see https://github.com/leforestier/yattag/issues/20
            self._append(strg)

    def nl(self):
        self._append('\n')

    def attr(self, *args, **kwargs):
        self.current_tag.attrs.update(_attributes(args, kwargs))

    def data(self, *args, **kwargs):
        self.attr(
            *(('data-%s' % key, value) for (key, value) in args),
            **dict(('data-%s' % key, value) for (key, value) in kwargs.items())
        )

    def stag(self, tag_name, *args, **kwargs):
        if args or kwargs:
            self._append("<%s %s%s" % (
                tag_name,
                dict_to_attrs(_attributes(args, kwargs)),
                self._stag_end
            ))
        else:
            self._append("<%s%s" % (tag_name, self._stag_end))

    def cdata(self, strg, safe = False):
        self._append('<![CDATA[')
        if safe:
            self._append(strg)
        else:
            self._append(strg.replace(']]>', ']]]]><![CDATA[>'))
        self._append(']]>')

    def getvalue(self):
        return ''.join(self.result)

    def tagtext(self):
        return self, self.tag, self.text

    def ttl(self):
        return self, self.tag, self.text, self.line

    def add_class(self, *classes):
        self._set_classes(
            self._get_classes().union(classes)
        )

    def discard_class(self, *classes):
        self._set_classes(
            self._get_classes().difference(classes)
        )

    def toggle_class(self, elem, active):
        classes = self._get_classes()
        if active:
            classes.add(elem)
        else:
            classes.discard(elem)
        self._set_classes(classes)


    def _get_classes(self):
        try:
            current_classes = self.current_tag.attrs['class']
        except KeyError:
            return set()
        else:
            return set(current_classes.split())

    def _set_classes(self, classes_set):
        if classes_set:
            self.current_tag.attrs['class'] = ' '.join(classes_set)
        else:
            try:
                del self.current_tag.attrs['class']
            except KeyError:
                pass


def html_escape(s):
    if isinstance(s,(int,float)):
        return str(s)
    try:
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    except AttributeError:
        raise TypeError(
            "You can only insert a string, an int or a float inside a xml/html text node. "
            "Got %s (type %s) instead." % (repr(s), repr(type(s)))
        )


def attr_escape(s):
    if isinstance(s,(int,float)):
        return str(s)
    try:
        return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    except AttributeError:
        raise TypeError(
            "xml/html attributes should be passed as strings, ints or floats. "
            "Got %s (type %s) instead." % (repr(s), repr(type(s)))
        )


ATTR_NO_VALUE = object()

def dict_to_attrs(dct):
    return ' '.join(
        (key if value is ATTR_NO_VALUE
        else '%s="%s"' % (key, attr_escape(value)))
        for key,value in dct.items()
    )

def _attributes(args, kwargs):
    lst = []
    for arg in args:
        if isinstance(arg, tuple):
            lst.append(arg)
        elif isinstance(arg, str):
            lst.append((arg, ATTR_NO_VALUE))
        else:
            raise ValueError(
                "Couldn't make a XML or HTML attribute/value pair out of %s."
                % repr(arg)
            )
    result = dict(lst)
    result.update(
        (('class', value) if key == 'klass' else (key, value))
        for key,value in kwargs.items()
    )
    return result


doc, tag, text = PyWeb().tagtext()

with tag('html'):
    with tag('body', id = 'hello'):
        with tag('h1'):
            text('O primeiro teste')

generate()

