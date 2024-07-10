import React from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import Navbar from './components/Navbar';
import Connections from './components/Connections';
import Portfolio from './components/Portfolio';
import RiskExposure from './components/RiskExposure';
import Analysis from './components/Analysis';
import './styles.css';

const App = () => (
  <Router>
    <div>
      <Navbar />
      <Switch>
        <Route path="/connections" component={Connections} />
        <Route path="/portfolio" component={Portfolio} />
        <Route path="/risk-exposure" component={RiskExposure} />
        <Route path="/analysis" component={Analysis} />
        <Redirect from="/" to="/portfolio" />
      </Switch>
    </div>
  </Router>
);

export default App;