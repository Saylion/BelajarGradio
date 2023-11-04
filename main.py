import gradio as gr
import urllib.request
from argparse import ArgumentParser

def swap_visibility():
  return gr.update(visible=True), gr.update(visible=False), gr.update(value=''), gr.update(value=none)

def process_file_upload(file):
  return file.name, gr.update(value=file.name)

if __name__ == '__main__':
  parser = ArgumentParser(description='Hello World', add_help=True)
  parser.add_argument("--share", action="store_true", dest="share_enabled", default=False, help="Enable sharing")
  parser.add_argument("--listen", action="store_true", default=False, help="Make the WebUI reachable from your local network.")
  parser.add_argument('--listen-host', type=str, help="The hostname server will use.")
  parser.add_argument('--listen-port', type=int, help="The listening port that the server will use.")
  args = parser.parse_args()

  with gr.Blocks(title='Hello World') as app:
    gr.Label('This is my first Gradio', show_label=False)
    with gr.Accordion('Main Option'):
      with gr.Row():
        with gr.Column() as yt_link_col:
          song_input = gr.Text(label='Song Input', info='Link to a song on Youtube or full path to a local file. For file upload, click button below.')
          show_file_upload_button = gr.Button('Upload file instead')
        with gr.Column(visible=False) as file_upload_col:
          local_file = gr.File(label='Audio file')
          song_input_file = gr.UploadButton('Upload', file_types=['audio'], variant='primary')
          show_yt_link_button = gr.Button('Paste Youtube link/Path to local file instead')
          song_input_file.upload(process_file_upload, inputs=[song_input_file], outputs=[local_file, song_input])

          show_file_upload_button.click(swap_visibility, outputs=[file_upload_col, yt_link_col, song_input, local_file])
          show_yt_link_file.click(swap_visibility, outputs=[yt_link_col, file_upload_col, song_input, local_file])

app.launch(
  share=args.share_enabled,
  server_name=None if not args.listen else (args.listen_host or '0.0.0.0'),
  server_port=args.listen_port,
).queue(True)
