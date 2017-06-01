import Griddle from 'griddle-react'
import react from 'react'

//var data = $.getJSON('https://api.github.com/search/repositories?q=javascript&sort=stars');
$.getJSON('https://api.github.com/search/repositories?q=javascript&sort=stars', function(data){
    console.log(data)
});

//ReactDOM.render(
//    //<Griddle results={} showSettings={true} showFilter={true} settingsText={"设置"} />,
//    document.getElementById('example')
//);
