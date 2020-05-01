import React from "react";
import PropTypes from "prop-types";

// import the Contact component
import Comic from "./Comic";

function ComicList(props) {
    return (
        <div>{props.comics.map(c => <Comic key={c.id} title={c.title} />)}</div>
    );
}

ComicList.propTypes = {
    comic: PropTypes.array.isRequired
};

export default ComicList;