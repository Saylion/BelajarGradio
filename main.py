import gradio as gr
import urllib.request
from argparse import ArgumentParser

if __name__ == '__main__':
  parser = ArgumentParser(description='Hello World', add_help=True)
  parser.add_argument("--share", action="store_true", dest="share_enabled", default=False, help="Enable sharing")
  parser.add_argument("--listen", action="store_true", default=False, help="Make the WebUI reachable from your local network.")
  parser.add_argument('--listen-host', type=str, help="The hostname server will use.")
  parser.add_argument('--listen-port', type=int, help="The listening port that the server will use.")
  args = parser.parse_args()

  with gr.Blocks(title='Hello World') as app:
      gr.Label('This is my first Gradio', show_label=False)

app.launch(
  share=args.share_enabled,
  enable_queue=True,
  server_name=None if not args.listen else (args.listen_host or '0.0.0.0'),
  server_port=args.listen_port,
)
