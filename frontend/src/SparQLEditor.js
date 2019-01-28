import React, { Component } from "react"; 
import scriptLoader from 'react-async-script-loader';

class SparQLEditor extends Component {
  componentDidMount() {
  }
  render() {
    return (
      <div className="sparqlEditor">
        <div id="yasqe"></div>
        <div id="yasr"></div>
      </div>
    );
  }
}

export default scriptLoader(
  [
    'http://cdn.jsdelivr.net/yasqe/2.2/yasqe.bundled.min.js',
    'http://cdn.jsdelivr.net/yasr/2.4/yasr.bundled.min.js'
  ],
  "/yasgui.js"
)(SparQLEditor);