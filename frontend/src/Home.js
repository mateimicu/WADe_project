import React, { Component } from "react";
import Query1 from './Query1.js';
import Query2 from './Query2.js';
 
class Home extends Component {
  render() {
    return (
      <div className="hardcodedQueries">
        <Query1/>
        <Query2/>
      </div>
    );
  }
}
 
export default Home;