tshark -r torrent.pcap -Y 'bittorrent.piece.index' -Tfields -e bittorrent.piece.index  > indexes

Opened in text editor, replaced commas (",") with line break ("\n") to get all indices on separate lines.
Copied list into excel, removed duplicates, got total pieces.

tshark -r torrent.pcap -Y 'bittorrent.piece.data' -Tfields -e bittorrent.piece.index -e bittorrent.piece.data > packets
