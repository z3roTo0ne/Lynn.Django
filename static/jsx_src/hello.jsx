//var React = require('react'); // ES5的写法
//import React from 'react'; // 这种是ES6的写法
//var linkState = require('react-link-state');

import React from 'react';
import linkState from 'react-link-state';
//
//var HelloWorldComponent = React.createClass({
//    displayName: 'HelloWorldComponent',
//    render: function() {
//        return (
//            //<div>Hello {this.props.name}</div>
//            <div>Hello ndddd</div>
//        );
//    }
//});


//class HelloWorldComponent extends React.Component {
//    constructor() {
//        super();
//        this.state = {};
//    }
//    render() {
//        return (
//            <div>Hello {this.props.name}</div>
//        );
//    }
//}


// ES6的方式高逼格编码， ES6绑定事件
// class LikeButton extends React.Component{
//    constructor(props){
//        super(props);
//        this.state = {liked: false};
//        // ES6的写法 React.createClass会自动绑定到类实例上，React.Component要通过以下方式来绑定
//        this.handleClick = this.handleClick.bind(this)
//    }
//
//    handleClick(){
//        this.setState({liked: !this.state.liked})
//    }
//
//    render() {
//        var text = this.state.liked ? 'like' : 'haven\'t liked';
//        return (
//            <p onClick={this.handleClick}>
//                You {text} this. Click to toggle.
//            </p>
//        );
//    }
//
//}


// 动态获取输入状态
// class YourInput extends React.Component{
//    constructor(props){
//        super(props);
//        this.state = {value: ""};
//        this.handleChange = this.handleChange.bind(this);
//
//    }
//
//    handleChange(event){
//        var your_value = event.target.value;
//        this.setState({value: your_value});
//    }
//
//    render(){
//        var value = this.state.value;
//        return (
//            <div>
//                <input type="text" value={value} onChange={this.handleChange}/>
//                <p>{value}</p>
//            </div>
//        )
//    }
//}



////遍历集合
// class MultiChoice extends React.Component {
//    constructor() {
//        this.state = {
//            data: ["Apple", "Banana", "juice"]
//        }
//    }
//    render(){
//        var data = this.state.data;
//        return(
//            <div>
//                <select>
//                    {data.map(function(result){
//                        return <option>{result}</option>
//                        })}
//                </select>
//
//            </div>
//        )
//    }
//}


//class WithLink extends React.Component{
//    constructor(props) {
//        super(props);
//        this.state = {
//            username: '',
//            password: '',
//            toggle: false
//        };
//    }
//    render() {
//        return (
//            <div>
//                <form>
//                    <input type="text" valueLink={linkState(this, 'username')} />
//                    <input type="password" valueLink={linkState(this, 'password')} />
//                </form>
//                <p> {this.state.username},xxx </p>
//            </div>
//        );
//    }
//}


//class Test extends React.Component{ //静态方法
//    static PrintContent(foo) {
//        return foo == "bar";
//    }
//    render(){
//    }
//}



//console.log(Test.PrintContent("bar"));
//ReactDOM.render(
//    <WithLink />,
//    document.getElementById("example")
//);



