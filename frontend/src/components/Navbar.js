import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => (
  <nav>
    <ul>
      <li><Link to="/connections">Connections</Link></li>
      <li><Link to="/portfolio">Portfolio</Link></li>
      <li><Link to="/risk-exposure">Risk/Exposure</Link></li>
      <li><Link to="/analysis">Analysis</Link></li>
    </ul>
  </nav>
);

export default Navbar;