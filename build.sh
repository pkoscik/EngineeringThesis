#!/usr/bin/env bash
ARGS=""

usage() {
  echo -e "Avabile flags:"
  echo -e "   -b: builds a .pdf file"
  echo -e "   -c: performs a \"small\" clean-up"
  echo -e "   -C: performs a \"big\" clean-up" 
}

# Check if any argument was passed
if [ $# -eq 0 ]
  then
    echo "No arguments supplied!"
    usage
    exit
fi

# Parse flags
while getopts bcCh flag 2>/dev/null
do
  case "${flag}" in
    b) ARGS+="-pdf";;
    c) ARGS+="-c";;
    C) ARGS+="-C";;
    h)
      echo "A small script to streamline the usage of texlive docker image."
      usage
      exit
      ;;
    *)
      echo "Unexpected flags!"
      usage
      exit
      ;;
  esac
done

# Run texlive image
sudo docker run -v $PWD:/files -w /files texlive/texlive latexmk ${ARGS}
