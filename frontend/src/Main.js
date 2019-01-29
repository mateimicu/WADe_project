import React, { Component } from "react";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Home from "./Home";
import SparQLEditor from "./SparQLEditor";
import logo from "./logo.png"
 
class Main extends Component {
  render() {
    return (
      <HashRouter>
        <div>
          <div className="container center">
            <nav className="menu">
              <h1 style={{'backgroundImage' : 'url(' + logo + ')'}} className="menu__logo">Disyo</h1>

              <div className="menu__right">
                <ul className="menu__list">
                  <li className="menu__list-item"><NavLink className="menu__link" exact to="/">Home</NavLink></li>
                  <li className="menu__list-item"><NavLink className="menu__link" to="/sparqleditor" onClick={() => {window.location.reload();}}>SparQL Editor</NavLink></li>
                  <li className="menu__list-item"><NavLink className="menu__link" to="/graphqlendpoint">GraphQL Endpoint</NavLink></li>
                  <li className="menu__list-item"><NavLink className="menu__link" to="/api">REST API</NavLink></li>
                </ul>
              </div>
            </nav>
          </div>
          <div className="content">
            <Route exact path='/' component={Home}/>
            <Route path="/sparqleditor" component={SparQLEditor}/>
            <Route path="/graphqlendpoint" component={() => {window.location = 'http://api.disyo.xyz/graphql/';}}/>
            <Route path="/api" component={() => {window.location = 'http://api.disyo.xyz/demo/';}}/>
          </div>
        </div>
      </HashRouter>
    );
  }
}
 
export default Main;
