from utils import create_input_files
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create input files')

    parser.add_argument('--dataset', '-d', default='flickr8k', help='dataset')
    parser.add_argument('--img_folder', '-i', default='image_folder', help='path to image')
    parser.add_argument('--caption_folder', '-cf', default='caption_datasets', help='path to captions')
    parser.add_argument('--glove', '-g', default='glove.6B.50d.txt', help='path to emd_file')

    args = parser.parse_args()

    # Create input files (along with word map)
    create_input_files(dataset=args.dataset,
                       karpathy_json_path='AdaptiveAttend/caption_datasets/dataset_flickr8k.json',
                       image_folder=args.img_folder,
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='{:s}_folder'.format(args.dataset),
                       glove=args.glove, max_len=50)
