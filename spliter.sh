#!/bin/bash

# Check if the input file is provided
if [ $# -eq 0 ]; then
    echo "File name to be split."
    exit 1
fi

# Set the input file name
input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "File not found: $input_file"
    exit 1
fi

# Calculate the number of 100 MB chunks
chunk_size=$((100 * 1024 * 1024))  # 100 MB in bytes
num_chunks=10

# Split the file into 100 MB chunks
split -b "$chunk_size" "$input_file" "$input_file.part"

# Rename the split files
for ((i=0; i<num_chunks; i++))
do
    mv "$input_file.part"$i "$input_file.part"$((i+1))
done

echo "File split successfully into $num_chunks 100 MB parts."
