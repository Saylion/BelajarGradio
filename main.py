import gradio as gr
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import numpy as np
import urllib.request
from argparse import ArgumentParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def video_splitting(local_file, progress=gr.Progress()):
  input_video = local_file
  output_dir = BASE_DIR

  subclip_start_times = [0, 30, 60]
  subclip_end_times = [30, 60, 90]

  for i, (start_time, end_time) in enumerate(zip(subclip_start_times, subclip_end_times)):
    output_file = f"{output_dir}subclip_{i}.mp4"
    ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_file)

def swap_visibility():
  return gr.update(visible=True), gr.update(visible=False), gr.update(value=''), gr.update(value=None)

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
        with gr.Column() as file_upload_col:
          local_file = gr.Text(label='Video file')
          input_file = gr.UploadButton('Upload', file_types=['video'], variant='primary')
          input_file.upload(process_file_upload, inputs=[input_file], outputs=[local_file])

        with gr.Row():  
          generate_btn = gr.Button("Generate", variant='primary')
          hasil = gr.Video(label='hasil')
        generate_btn.click(video_splitting, inputs=[local_file], outputs=[hasil])
          
'''
          show_file_upload_button.click(swap_visibility, outputs=[file_upload_col, yt_link_col, song_input, local_file])
          show_yt_link_button.click(swap_visibility, outputs=[yt_link_col, file_upload_col, song_input, local_file])
          '''
app.launch(
  share=args.share_enabled,
  server_name=None if not args.listen else (args.listen_host or '0.0.0.0'),
  server_port=args.listen_port,
  enable_queue=True
)
