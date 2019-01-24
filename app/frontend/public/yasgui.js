var yasqe = YASQE(document.getElementById("yasqe"), {
  sparql: {
    showQueryButton: true
  }
});
var yasr = YASR(document.getElementById("yasr"), {
  getUsedPrefixes: yasqe.getPrefixesFromQuery
});

yasqe.options.sparql.callbacks.complete = yasr.setResponse;
/* yasqe.options.sparql.endpoint = 'http://localhost:3030/disyo/query'; */