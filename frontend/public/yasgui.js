var yasqe = YASQE(document.getElementById("yasqe"), {
  sparql: {
    showQueryButton: true,
    endpoint: "http://127.0.0.1:3030/disyo/query"
  }
});
var yasr = YASR(document.getElementById("yasr"), {
  getUsedPrefixes: yasqe.getPrefixesFromQuery
});

yasqe.options.sparql.callbacks.complete = yasr.setResponse;

var url = window.location.href;
var res = url.match(/sparqleditor\?([^&]*)/);
if (res != null) {
  var query = decodeURI(res[1]);
  yasqe.setValue(query);
}
