import React from "react";
import { NavLink } from "react-router-dom";

const Navigation = () => {
  return (
    <nav className="main-nav">
      <ul>
        <li>
          <NavLink to="/mountain">Features</NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
