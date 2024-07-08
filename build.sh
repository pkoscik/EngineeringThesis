#!/usr/bin/env bash
ARGS=""
UPDATE=false

usage() {
  echo -e "Avabile flags:"
  echo -e "   -b: builds a .pdf file"
  echo -e "   -c: performs a \"small\" clean-up"
  echo -e "   -C: performs a \"big\" clean-up" 
  echo -e "   -u: Send a SIGHUP signal to all MuPDF processes after compilation"
}

# Check if any argument was passed
if [ $# -eq 0 ]
  then
    echo "No arguments supplied!"
    usage
    exit
fi

# Parse flags
while getopts bcChu flag 2>/dev/null
do
  case "${flag}" in
    b) ARGS+="-pdf";;
    c) ARGS+="-c";;
    C) ARGS+="-C";;
    u) UPDATE=true;;
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

# Send a update signall to all MuPDF instances
if $UPDATE; then
    echo "Sending a SIGHUP to all MuPDF instances!"
    pkill -SIGHUP mupdf
fi
  