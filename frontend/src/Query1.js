import React, { Component } from "react";
import { withRouter } from 'react-router-dom';
 
class Query1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
        githubStars : 0,
        license: 'NotOpenSource',
        applicationCategory: "Provisioning",
        applicationSubCategory: "Automation & Configuration",

    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    console.log(event.target)
    var url = "/sparqleditor?";
    var query = `
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT *
WHERE {
   ?subject <https://schema.org/docs/schemaorg.owl#applicationSubCategory> "${this.state.applicationSubCategory}" .
   ?subject <https://schema.org/docs/schemaorg.owl#applicationCategory> "${this.state.applicationCategory}" .
   ?subject <http://api.disyo.xyz/api/dsapplications/license> "${this.state.license}" .
   ?subject <http://api.disyo.xyz/api/dsapplications/githubStars> ?githubStars .
   FILTER ( ?githubStars >= "${this.state.githubStars}"^^xsd:integer ) .
}
LIMIT 100
`
    var queryUrl = encodeURI(url + query);
    console.log(queryUrl);
    event.preventDefault();
    this.props.history.push(queryUrl);
    window.location.reload();
  }

  render() {
    return (
      <details open>
        <summary> Filter on the popularity of the project.</summary>
        <form onSubmit={this.handleSubmit}>
          <label>
            GithubStars:&nbsp;
            <input name="githubStarts" type="number" value={this.state.githubStars} onChange={this.handleChange} /> 
          </label>


          <label>
            License:&nbsp;
            <input name="license" type="text" value={this.state.license} onChange={this.handleChange} />
          </label>


          <label>
            Application Category:&nbsp;
            <input name="applicationCategory" type="text" value={this.state.applicationCategory} onChange={this.handleChange} />
          </label>

          <label>
            Application SubCategory:&nbsp;
            <input name="applicationSubCategory" type="text" value={this.state.applicationSubCategory} onChange={this.handleChange} />
          </label>

          <input type="submit" value="Run Query" />
        </form>
      </details>
    );
  }
}
 
export default withRouter(Query1);
