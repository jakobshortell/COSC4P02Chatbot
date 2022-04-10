import React from "react";

import dotCSS from "../css/Dot.css"

//might need this if we want to do any influencing with JS later
const Dot = ({Dot}) =>{

    return (
       <div id = "activedot" className="Chatbot-active">
        <div className="active-chatbot-dot"></div></div>
    );

}


export default Dot;