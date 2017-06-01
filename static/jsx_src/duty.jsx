import Griddle from 'griddle-react'

function apiStatus(){
    console.log("hhh")
}
class DutyList extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            dutyList:[]
        }
    }

    componentWillUnmount() {
        this.mounted = false;
    }

    componentDidMount(){
        this.mounted = true;
        var _this = this;
        $.ajax({
            url: this.props.source,
            type: "GET",
            dataType: "JSON",
            success: function(result){
                _this.setState({ dutyList: result});
            },
            error: function(XMLHttpRequest, textStatus, errorThrown){
                console.log(XMLHttpRequest, textStatus, errorThrown)
            }
        });

    }

    render(){
        var columnMeta =[
            {
                "columnName": "date",
                "order": 1,
                "locked": false,
                "visible": true,
                "displayName": "值班日期"
            },
            {
                "columnName": "duty_type",
                "order": 2,
                "locked": false,
                "visible": true,
                "displayName": "值班类型"
            },
            {
                "columnName": "email",
                "order": 3,
                "locked": false,
                "visible": true,
                "displayName": "个人邮箱"
            },
            {
                "columnName": "duty_name",
                "order": 4,
                "locked": false,
                "visible": true,
                "displayName": "值班人员"
            },
            {
                "columnName": "maintenance",
                "order": 5,
                "locked": false,
                "visible": true,
                "displayName": "维护人员"
            }
        ];
        return <Griddle results={this.state.dutyList} showSettings={true} showFilter={true} settingsText={"设置"}
                        resultsPerPage={10} filterPlaceholderText={"快速过滤"} nextText={"下一页"} previousText={"上一页"}
                        noDataMessage={"数据为空"} columnMetadata={columnMeta}/>
    }
}

ReactDOM.render(
    <DutyList source="http://esb.service.digi-sky.com/esb/duty/100/" />,
    document.getElementById("duty")
);