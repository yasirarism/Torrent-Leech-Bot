export MAX_DOWNLOAD_SPEED=0
export MAX_CONCURRENT_DOWNLOADS=3
aria2c --enable-rpc --rpc-listen-all=false --rpc-max-request-size=1024M \
  --max-connection-per-server=10 --check-certificate=false --rpc-listen-port 6800 \
  --seed-time=0.01 --follow-torrent=mem --split=10 --min-split-size=10M \
   --daemon=true --allow-overwrite=true --max-overall-download-limit=$MAX_DOWNLOAD_SPEED \
   --max-concurrent-downloads=$MAX_CONCURRENT_DOWNLOADS --max-overall-upload-limit=1K 
