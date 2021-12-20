import os
import cv2
import argparse
from tqdm import tqdm
from random import random
from os import path as osp


def filter_file_from_extension(file_list, extension):
    return [fn for fn in file_list if fn.lower().endswith(extension)]


def create_dir_if_not_exists(path):
    os.makedirs(path, exist_ok=True)

def remove_all_files_from_list(list_files, directory):
    for fn in list_files:
        os.remove(fn)

def save_frames(video_path, frame_ratio, output_path, video_length=None):
    print(video_path)
    saved_frames = []
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened() is False:
        return None
    if video_length is None:
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if isinstance(frame_ratio, int):
        pace_frame = int(video_length // frame_ratio)
    else:
        pace_frame = int(1 // frame_ratio)
    
    idx = 0
    for idx in tqdm(range(video_length)):
        ret, frame = cap.read()
        if ret is False:
            remove_all_files_from_list(saved_frames, osp.dirname(output_path))
            print(f'Wrong number of frames, trying again with {idx}')
            save_frames(video_path, frame_ratio, output_path, video_length=idx)
            return
        if idx % pace_frame == 0:
            out = f'{output_path}_{idx}.png'
            saved_frames.append(out)
            cv2.imwrite(out, frame)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', '-i', type=str, help='Input root folder')
    parser.add_argument('--output-dir', '-o', type=str, help='output root folder')
    parser.add_argument('--frames', '-n', type=str, help='Frame rate or number of frames')
    parser.add_argument('--extension', '-e', type=str, default='MP4', help='Video Extension')
    args = vars(parser.parse_args())
    
    frame_rate = float(args['frames']) if '.' in args['frames'] else int(args['frames'])

    create_dir_if_not_exists(args['output_dir'])
    extension = args['extension'].lower()

    for root, dir, fns in os.walk(args['input_dir']):
        print(f'Searching videos from {root}')
        videos = filter_file_from_extension(fns, extension)
        if len(videos):
            output_folder_path = root.replace(args['input_dir'], args['output_dir'])
            create_dir_if_not_exists(output_folder_path)
            print('Taking frames from videos')
            for video in videos:
                save_frames(osp.join(root, video), frame_rate, osp.join(output_folder_path, video))
