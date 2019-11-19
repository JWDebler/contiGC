# contiGC
determine per contig / scaffold GC content

# Requirements
- numpy
- plotly
- requests
- psutil

# To Do
- [x] import contigs fasta
- [ ] fix reading fastas with several lines, currently something strange going on
- [x] calculate per contig GC content and put into a list
- [x] sort list by gc content
- [ ] plot gc content as histogram (plotly)
- [ ] option to export contigs within a GC range