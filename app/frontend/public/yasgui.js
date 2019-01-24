var yasqe = YASQE(document.getElementById("yasqe"), {
  sparql: {
    showQueryButton: true,
    endpoint: "http://lod.openlinksw.com/sparql/"
  }
});
var yasr = YASR(document.getElementById("yasr"), {
  getUsedPrefixes: yasqe.getPrefixesFromQuery
});

yasqe.options.sparql.callbacks.complete = yasr.setResponse;

var url = window.location.href;
var query = decodeURI(url.match(/sparqleditor\?([^&]*)/)[1]);
yasqe.setValue(query);