import React, { Component } from "react";
import { withRouter } from 'react-router-dom';
import queryString from 'query-string';
 
class Query1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
        githubStars : 0,
        // license: 'NotOpenSource',
        license: "Any",
        applicationCategory: "Any",
        applicationSubCategory: "Any",
        rez: [],
		licenses_list: ["Any"],
        applicationCategory_list : ["Any"],
        applicationSubCategory_list: ["Any"],
    };
    let getLicensesQuery = `
    SELECT ?license 
	WHERE {
	?subject http://sparql.disyo.xyz/disyo/license> ?license
	}
	GROUP BY ?license
      `

    let getSubCategoryQuery = `
SELECT ?subCategory
WHERE {
  ?subject <https://schema.org/docs/schemaorg.owl#applicationSubCategory> ?subCategory

}
GROUP BY ?subCategory

      `

    let getCategoryQuery = `
    SELECT ?category
	WHERE {
	?subject <https://schema.org/docs/schemaorg.owl#applicationCategory> ?category
	}
	GROUP BY ?category
      `
    let aux = this;
	// licenses fetch
    fetch("http://sparql.disyo.xyz/disyo/query", 
        {headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'application/json',
            },
         method: "POST",
         body: queryString.stringify({query: getLicensesQuery})
        })
    .then(function(res){ 
        res.json().then(json_data => {
            json_data.results.bindings.forEach(data => {
                aux.state.licenses_list.push(
                    data.license.value,
                );
				aux.forceUpdate();
            })
        });
    })
    .catch(
        function(res){ console.log(res) 
    })

	// cattegory
    fetch("http://sparql.disyo.xyz/disyo/query", 
        {headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'application/json',
            },
         method: "POST",
         body: queryString.stringify({query: getCategoryQuery})
        })
    .then(function(res){ 
        res.json().then(json_data => {
            json_data.results.bindings.forEach(data => {
                aux.state.applicationCategory_list.push(
                    data.category.value,
                );
				aux.forceUpdate();
            })
        });
    })
    .catch(
        function(res){ console.log(res) 
    })

	// sub cattegory
    fetch("http://sparql.disyo.xyz/disyo/query", 
        {headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'application/json',
            },
         method: "POST",
         body: queryString.stringify({query: getSubCategoryQuery})
        })
    .then(function(res){ 
        res.json().then(json_data => {
            json_data.results.bindings.forEach(data => {
                aux.state.applicationSubCategory_list.push(
                    data.subCategory.value,
                );
				aux.forceUpdate();
            })
        });
    })
    .catch(
        function(res){ console.log(res) 
    })


    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
	// update in case of category change
	if (event.target.name === "applicationCategory"){
		let aux = this;
		let match = ".*";
		if (event.target.value !== "Any"){
			match = event.target.value;
		}
		let getSubCategoryQuery = `
SELECT ?subCategory
WHERE {
  ?subject <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> http://sparql.disyo.xyz/disyo/DSApplication> .
          ?subject <https://schema.org/docs/schemaorg.owl#applicationCategory> ?applicationCategory .
          ?subject <https://schema.org/docs/schemaorg.owl#applicationSubCategory> ?subCategory.
  FILTER( regex(?applicationCategory, "${match}")  ) .

}
GROUP BY ?subCategory

		`

    fetch("http://sparql.disyo.xyz/disyo/query", 
        {headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'application/json',
            },
         method: "POST",
         body: queryString.stringify({query: getSubCategoryQuery})
        })
    .then(function(res){ 
        res.json().then(json_data => {
			let aux_list = ["Any"]
            json_data.results.bindings.forEach(data => {
                aux_list.push(
                    data.subCategory.value,
                );
            })
			console.log("fetch", aux_list)
			aux.setState({applicationSubCategory_list: aux_list});
        });
    })
    .catch(
        function(res){ console.log(res) 
    })
	}
  }

  handleSubmit(event) {
	let match_license= (this.state.license === "Any") ? ".*" : this.state.license;
	let match_applicationCategory= (this.state.applicationCategory === "Any") ? ".*" : this.state.applicationCategory;
	let match_applicationSubCategory = (this.state.applicationSubCategory === "Any") ? ".*" : this.state.applicationSubCategory;
	console.log(match_license, this.state);
    var sparqlQuery = `
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#> 
SELECT ?name ?githubStars ?logoURI ?homepage ?subject ?applicationCategory ?applicationSubCategory ?license
WHERE {   
  ?subject <https://schema.org/docs/schemaorg.owl#applicationSubCategory>  ?applicationSubCategory . 
  ?subject <https://schema.org/docs/schemaorg.owl#applicationCategory> ?applicationCategory . 
  ?subject http://sparql.disyo.xyz/disyo/license> ?license .  
  ?subject http://sparql.disyo.xyz/disyo/githubStars> ?githubStars . 
  ?subject http://sparql.disyo.xyz/disyo/logoURI> ?logoURI .  
  ?subject http://sparql.disyo.xyz/disyo/homepage> ?homepage. 
  ?subject <https://schema.org/docs/schemaorg.owl#name>  ?name.  
  FILTER ( ?githubStars >= "${this.state.githubStars}"^^xsd:integer  ) .
  FILTER( regex(?license, "${match_license}")  ) .
  FILTER( regex(?applicationCategory, "${match_applicationCategory}")  ) .
  FILTER( regex( ?applicationSubCategory, "${match_applicationSubCategory}" )  ) .
} ORDER BY DESC(?githubStars) LIMIT 30
`

    let aux = this;

    // query the sparql and list items
    fetch("http://sparql.disyo.xyz/disyo/query", 
        {headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'application/json',
            },
         method: "POST",
         body: queryString.stringify({query: sparqlQuery})
        })
    .then(function(res){ 
        aux.setState({
            rez: []
        });

        res.json().then(json_data => {
            json_data.results.bindings.forEach(data => {
                console.log(data);
                aux.state.rez.push([
                    data.logoURI.value,
                    data.homepage.value,
                    data.name.value,
                    data.githubStars.value,
 					data.applicationCategory.value,
					data.applicationSubCategory.value,
					data.license.value,
                ]);
                aux.setState({rez: aux.state.rez});
            })
        });
    })
    .catch(
        function(res){ console.log(res) 
    })

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
			<select name="license" value={this.state.license} onChange={this.handleChange}>
            {this.state.licenses_list.map(function(name, index){
                return <option key={index} value={name}> {name}</option>
                })
            }
			</select>
          </label> <br></br>


          <label>
            Application Category:&nbsp;
			<select name="applicationCategory" value={this.state.applicationCategory} onChange={this.handleChange}>
            {this.state.applicationCategory_list.map(function(name, index){
                return <option key={index} value={name}> {name}</option>
                })
            }
			</select>
          </label>

          <label>
            Application SubCategory:&nbsp;
			<select name="applicationSubCategory" value={this.state.applicationSubCategory} onChange={this.handleChange}>
            {this.state.applicationSubCategory_list.map(function(name, index){
                return <option key={index} value={name}> {name}</option>
                })
            }
			</select>
          </label>

          <input type="submit" value="Run Query" />
        </form>
        <div>
           <table >
          <thead>
            <tr>
                <th>Logo</th>
                <th>Name</th>
                <th>GitHub Stars</th>
                <th>Application Category</th>
                <th>Application SubCategory</th>
                <th>License</th>
            </tr>
          </thead>

          <tbody>
            {this.state.rez.map(function(name, index){
                return <tr key={index}>
                <td><a href={name[1]}> <img alt={name[2]} src={name[0]}></img> </a> </td>
                <td><a href={name[1]}> {name[2]} </a></td>
                <td>{name[3]}</td>
                <td>{name[4]}</td>
                <td>{name[5]}</td>
                <td>{name[6]}</td>
                </tr>;
                })
            }
          </tbody>
            </table> 
        </div>
      </details>
    );
  }
}
 
export default withRouter(Query1);
