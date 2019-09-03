import gi
gi.require_version("WebKit2", "4.0")

from gi.repository import WebKit2, Gtk, GLib
import sys
import os

mydir = os.path.join(os.path.dirname(__file__))
ctx = WebKit2.WebContext.get_default()
ctx.set_web_extensions_directory(mydir)	
wnd = Gtk.Window()
wnd.set_title('Pagina')
web = WebKit2.WebView.new_with_context(ctx)
wnd.connect("destroy", Gtk.main_quit)
wnd.add(web)
wnd.set_default_size(1152, 800)
wnd.show_all()
web.load_uri("https://web.whatsapp.com/")

Gtk.main()
