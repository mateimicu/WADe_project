import React, { Component } from "react";
import { withRouter } from 'react-router-dom';
 
class Query2 extends Component {
  constructor(props) {
    super(props);
    this.state = {value: '0'};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    console.log(this.state.value);
    var url = "/sparqleditor?";
    var query = "select * where { ?sub ?pred ?obj.} limit 10";
    var queryUrl = encodeURI(url + query);
    event.preventDefault();
    this.props.history.push(queryUrl);
    window.location.reload();
  }

  render() {
    return (
      <details>
        <summary> descriere query2</summary>
        <form onSubmit={this.handleSubmit}>
          <label>
            count ceva:&nbsp;
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Run Query" />
        </form>
      </details>
    );
  }
}
 
export default withRouter(Query2);