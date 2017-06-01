import React from 'react'
import ReactDOM from 'react-dom'

import classNames from 'classnames/bind'


class SearchPanel extends React.Component{
    render(){
        return(
            <div className="col-md-12 col-sm-12 col-xs-12 form-group">
                <div className="input-group">
                    <input ref="search" type="text" className="form-control input-sm" value={this.props.search} onChange={this.onSearchChanged.bind(this)}/>
                    <span className="input-group-btn">
                        {this.props.search?<button className="btn btn-default" type="button">清除</button>:null}
                    </span>
                </div>
            </div>
        )
    }
    onSearchChanged(){
        let search_value = React.findDOMNode(this.refs.search).value;
        this.props.onSearchChanged(search_value)
    }
}

var NotifyMessage = (props) => {    /* 消息通知组件 这是一个无状态组件 */
    "use strict";
    let msg_class = classNames(
        'alert alert-dismissible fade in',
        props.msgTypeClass //这个是定义通知类型 success、danger、info、primary
    );
    return (
        <div className={props.alertPanelClass} id={props.id}>
            <div className={msg_class} role="alert">
                <button onClick={props.handleRemoveMessage} type="button" className="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">×</span></button>
                <strong><i className={props.iconClass}></i>{props.msgTypeCount}</strong> &nbsp; <span>{props.messageContent}</span>
            </div>
        </div>
    )
};

// class NotifyMessage extends React.Component{    /* 消息通知组件 */
//     render(){
//         let msg_class = classNames(
//             'alert alert-dismissible fade in',
//             this.props.msgTypeClass //这个是定义通知类型 success、danger、info、primary
//         );
//         return (
//             <div className={this.props.alertPanelClass} id={this.props.id}>
//                 <div className={msg_class} role="alert">
//                         <button onClick={this.props.handleRemoveMessage} type="button" className="close" data-dismiss="alert" aria-label="Close">
//                         <span aria-hidden="true">×</span></button>
//                     <strong><i className={this.props.iconClass}></i>{this.props.msgTypeCount}</strong> &nbsp; <span>{this.props.messageContent}</span>
//                 </div>
//             </div>
//         )
//     }
// }

class EditForm extends React.Component{

    render(){
        let author_options = []; //把所有的作者读出来，便于写在select的下拉菜单选项中
        if(this.props.authors.results){
            this.props.authors.results.forEach(au => {
                author_options.push(<option key={au.id} value={au.salutation}>{au.salutation}</option>)
            });
        }

        let publisher_options = [];
        if(this.props.publisher.results){
            this.props.publisher.results.forEach(pu => {
                publisher_options.push(<option key={pu.id} value={pu.name}>{pu.name}</option>)
            });
        }

        return(
            <form className="form-horizontal form-label-left" onSubmit={this.props.handleSubmitClick} method="post">
                <div className="form-group">
                    <label className="control-label col-md-3 col-sm-3 col-xs-12" htmlFor="book-title"> 书名</label>
                    <div className="col-md-9 col-sm-9 col-xs-12">
                        <input value={this.props.book.title} ref='title' onChange={this.onChange.bind(this)} type="text" id="book-title" required="required" className="form-control" />
                    </div>
                </div>
                <div className="form-group">
                    <label className="control-label col-md-3 col-sm-3 col-xs-12" htmlFor="book-authors"> 作者 </label>
                    <div className="col-md-9 col-sm-9 col-xs-12">
                        <select value={this.props.book.author} ref='authors' onChange={this.onChange.bind(this)} id="book-authors" className="form-control">
                            {author_options}
                        </select>
                    </div>
                </div>
                <div className="form-group">
                    <label className="control-label col-md-3 col-sm-3 col-xs-12" htmlFor="book-publisher"> 出版社 </label>
                    <div className="col-md-9 col-sm-9 col-xs-12">
                        <select value={this.props.book.publisher} ref='publisher' onChange={this.onChange.bind(this)} id="book-publisher" className="form-control">
                            {publisher_options}
                        </select>
                    </div>
                </div>
                <div className="form-group">
                    <div className="col-md-9 col-sm-9 col-xs-12 col-md-offset-3">
                        <input type="submit" className="btn btn-primary btn-sm" value={this.props.book.id?"保存 (id = " +this.props.book.id+ ")":"增加"}/>
                        {this.props.book.id?<button className="btn btn-danger btn-sm" onClick={this.props.handleDeleteClick}>删除</button>:null}
                        {this.props.book.id?<button className="btn btn-info btn-sm" onClick={this.props.handleCancelClick}>取消</button>:null}
                    </div>
                    {this.props.message == 'add ok'?
                        <NotifyMessage msgTypeClass="alert-success"
                                       iconClass="fa fa-check"
                                       alertPanelClass="col-md-9 col-sm-9 col-xs-12 col-md-offset-3"
                                       handleRemoveMessage={this.props.handleRemoveMessage}
                                       msgTypeCount="成功"
                                       messageContent="新增记录成功"
                        />:null}
                    {this.props.message == 'update ok'?
                        <NotifyMessage id="updateMsg" msgTypeClass="alert-info"
                                       iconClass="fa fa-check"
                                       alertPanelClass="col-md-9 col-sm-9 col-xs-12 col-md-offset-3"
                                       handleRemoveMessage={this.props.handleRemoveMessage}
                                       msgTypeCount="成功"
                                       messageContent="更新记录成功"
                        />
                        :null}
                    {this.props.message == 'delete ok'?
                        <NotifyMessage msgTypeClass="alert-danger"
                                       iconClass="fa fa-check"
                                       alertPanelClass="col-md-9 col-sm-9 col-xs-12 col-md-offset-3"
                                       handleRemoveMessage={this.props.handleRemoveMessage}
                                       msgTypeCount="成功"
                                       messageContent="删除记录成功"
                        />:null}
                    {this.props.message == 'disappear'?null:null}
                </div>
            </form>
        )
    }

    onChange(){
        let book_title = ReactDOM.findDOMNode(this.refs.title).value;
        let book_authors = ReactDOM.findDOMNode(this.refs.authors).value;
        let book_publisher = ReactDOM.findDOMNode(this.refs.publisher).value;
        this.props.handleChange(book_title, book_authors, book_publisher)
    }
}


class BookTableRow extends React.Component{
    render(){
        return (
            <tr>
                <td>{this.props.book.id}</td>
                <td>{this.props.book.title}</td>
                <td>{this.props.book.authors}</td>
                <td>{this.props.book.publisher}</td>
                <td><a href="#" onClick={this.onClick.bind(this)} className="btn btn-info btn-xs"><i className="fa fa-pencil"></i> 编辑 </a></td>
            </tr>
        )
    }

    onClick(id){
        this.props.handleEditClickPanel(this.props.book.id)
    }
}


class BookTable extends React.Component{
    render() {
        let rows = [];
        if(this.props.books.results){ //这里的if主要是解决了异步的时差问题，到底是不是这样，
            this.props.books.results.forEach(bk => {
                rows.push(<BookTableRow key={bk.id} book={bk} handleEditClickPanel={this.props.handleEditClickPanel} />);
            });
        }
        return (
            <table className={this.props.className}>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>书名</th>
                    <th>作者</th>
                    <th>出版社</th>
                    <th>操作</th>
                </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        );
    }
}


class BookPanel extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            message: "",
            search: "",
            books: [],
            authors: [],
            publisher: [],
            editingBook: {
                title: "",
                author: "",
                publisher: ""
            }
        };
        this.handleEditClickPanel = this.handleEditClickPanel.bind(this);
        this.reloadBooks = this.reloadBooks.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.searchBook = this.searchBook.bind(this);
        this.handleSubmitClick = this.handleSubmitClick.bind(this);
        this.handleDeleteClick = this.handleDeleteClick.bind(this);
        this.handleCancelClick = this.handleCancelClick.bind(this);
        this.handleRemoveMessage = this.handleRemoveMessage.bind(this);
    }

    reloadBooks(id){
        let bookBaseUrl = this.props.url+"books/";
        let queryUrl = id ? bookBaseUrl+id+"/?format=json": bookBaseUrl+"?format=json";
        return $.getJSON(queryUrl);
    }

    loadAuthors(){
        let authorBaseUrl = this.props.url+"authors/";
        return $.getJSON(authorBaseUrl+"?format=json");
    }


    loadPublisher(){
        let publisherBaseUrl = this.props.url+"publisher/";
        return $.getJSON(publisherBaseUrl+"?format=json");
    }

    componentDidMount(){
        let query_books = this.reloadBooks();
        query_books.then(books => {
            this.setState({books: books})
        });

        let query_authors = this.loadAuthors();
        query_authors.then(authors => {
            this.setState({authors: authors})
        });

        let query_publisher = this.loadPublisher();
        query_publisher.then(publisher => {
            this.setState({publisher: publisher})
        });

    }

    handleEditClickPanel(id){
        let query_data = this.reloadBooks(id);
        query_data.then(book => {
            this.setState({
                editingBook:{
                    id:id,
                    title:book.title,
                    author:book.authors,
                    publisher:book.publisher
                }
            })
        });
    }


    handleInputChange(book_title, book_authors, book_publisher){
        this.setState({
            editingBook:{
                id:this.state.editingBook.id,
                title:book_title,
                author:book_authors,
                publisher:book_publisher
            }
        })
    }

    searchBook(book){
        $.ajax({
            url:this.props.searchBookUrl,
            dataType: "JSON",
            cache: false,
            data: JSON.stringify({'book':book}),
            success: function (response) {
            }.bind(this)
        })
    }

    onSearchChanged(search){

    }

    handleSubmitClick(e){
        e.preventDefault();
        if(this.state.editingBook.id){
            $.ajax({
                url:this.props.saveOrUpdateUrl,
                type: "POST",
                dataType: "JSON",
                data: JSON.stringify(this.state.editingBook),
                cache: false,
                success: function (response) {
                    let new_data = this.reloadBooks();
                    new_data.then(books => {
                        this.setState({books: books})
                    });
                    this.setState({message: "update ok"});
                    this.setState({editingBook: ""});
                }.bind(this)
            })
        } else {
            $.ajax({
                url: this.props.saveOrUpdateUrl,
                type: "POST",
                dataType:"JSON",
                data: JSON.stringify(this.state.editingBook),
                cache: false,
                success: function (resopnse) {
                    this.setState({message: "add ok"});
                    let new_data = this.reloadBooks();
                    new_data.then(books => {
                        this.setState({books: books})
                    });
                }.bind(this)  //ajax是异步请求，必须要bind
            })
        }
    }

    handleDeleteClick(e){
        e.preventDefault();
        $.ajax({
            url: this.props.deleteUrl,
            type: "POST",
            dataType:"JSON",
            data: JSON.stringify(this.state.editingBook),
            cache: false,
            success: function (resopnse) {
                let new_data = this.reloadBooks();
                new_data.then(books => {
                    this.setState({books: books})
                });
                this.setState({message: "delete ok"});
                this.setState({editingBook: ""});

            }.bind(this)  //ajax是异步请求，必须要bind
        })
    }

    handleCancelClick(e){
        e.preventDefault();
        this.setState({editingBook:{}})
    }

    handleRemoveMessage(e){
        // 一切都是状态， 要把message的状态还原，不然页面会有bug
        e.preventDefault();
        this.setState({message: ""})
    }

    render(){
        return(
            <div className="row">
                <div className="col-md-6 col-sm-6 col-xs-12">
                    <SearchPanel onSearchChanged={this.onSearchChanged} />
                    <BookTable className="table table-striped responsive-utilities jambo_table bulk_action" books={this.state.books} handleEditClickPanel={this.handleEditClickPanel}/>
                </div>
                <div className="col-md-6 col-sm-6 col-xs-12">
                    <EditForm book={this.state.editingBook}
                              authors={this.state.authors}
                              publisher={this.state.publisher}
                              handleChange={this.handleInputChange}
                              handleSubmitClick={this.handleSubmitClick}
                              handleDeleteClick={this.handleDeleteClick}
                              handleCancelClick={this.handleCancelClick}
                              handleRemoveMessage={this.handleRemoveMessage}
                              message={this.state.message}
                    />
                </div>
            </div>
        )
    }
}

ReactDOM.render(
    <BookPanel url="/api/"
               searchBookUrl="/search_book/"
               saveOrUpdateUrl="/change_book/"
               deleteUrl="/delete_book/"
    />,
    document.getElementById("study")
);
