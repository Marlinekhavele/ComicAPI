import React from "react";
import PropTypes from "prop-types";
import "./Comic.css";

function Comic(props) {
    return (
        <div className="comic">
            <span>{props.title}</span>
        </div>
    );
}

Comic.propTypes = {
    title: PropTypes.string.isRequired
};

export default Comic;