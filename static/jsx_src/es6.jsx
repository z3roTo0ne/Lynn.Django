class HelloComponentOne extends React.Component{
    render(){
        return(
            <div>hello, {this.props.name}</div>
        )
    }
}

var HelloComponentTwo = (props) => {
    "use strict";
    return(
        <div>hello ,{props.name}</div>
    )
};

var HelloComponentThree = ({name}) => (
    <div>hello, {name}</div>
);


ReactDOM.render(
    <HelloComponentTwo name="chenlin2"/>,
    document.getElementById("es6")
);