import React, {Component} from 'react';
import {
    Badge,
    Card,
    CardBody,
    CardHeader,
    Col,
    Pagination,
    PaginationItem,
    PaginationLink,
    Row,
    Table
} from 'reactstrap';
import axios from 'axios';
import {BASEURL} from "../../../Constants";
// function getvals(){
//     return fetch('http://localhost:8000/message/listallmessages/',
//     {
//     	method: "GET",
//       headers: {
//         'Accept': 'application/json',
//         'Content-Type': 'application/json',
//       },
//     })
//     .then((response) => response.json())
//     .then((responseData) => {
//       //console.log(responseData);
//       return responseData;
//     })
//     .catch(error => console.warn(error));

//   }
class Tables extends Component {
    tableData;

    constructor(props) {
        super(props);
        this.state = {
            tableData: []
        }
    }

    componentDidMount() {
        axios.get(BASEURL + 'message/listallmessages/', {
            responseType: 'json'
        }).then(response => {
            this.state.tableData = response.data;
            console.log(this.state.tableData)
            // this.generateTableData()
        });
    }

    // getallmessages = (data) => {
    //     // make API call
    //     let tablesHTML = [];
    //     // this.setState({loading: true});
    //     let url = 'http://localhost:8000/message/listallmessages/';
    //     fetch(url, {
    //         method: "GET"
    //     }).then(response => {
    //         if (response.status === 200) {
    //               console.log(response);
    //             return response.json()
    //         } else {
    //                console.log("oh no!", response.status === 404)
    //         }
    //     }).then(function (data) {
    //         console.log('request succeeded with JSON response', data)
    //         return data
    //     })
    // }
    //
    generateTableData() {
        let res = [];
        // let tableData1 = this.tableData;
        console.log(this.state.tableData);

        this.state.tableData.map(message => (
            res.push(
                <tr>
                    <td key={message.from_who}>{message.from_who}</td>
                    <td key={message.to_who}>{message.to_who}</td>
                    <td key={message.message}>{message.message}</td>
                    <td key={message.id}>{message.id}</td>
                    <td key={message.message_status}>{message.message_status}</td>
                </tr>
            )
        ));
        // for (let tableData2 of tableData1) {
        //     res.push(
        //         <tr>
        //             <td key={tableData2.from_who}>{tableData2.from_who}</td>
        //             <td key={tableData2.to_who}>{tableData2.to_who}</td>
        //             <td key={tableData2.message}>{tableData2.message}</td>
        //             <td key={tableData2.id}>{tableData2.id}</td>
        //             <td key={tableData2.message_status}>{tableData2.message_status}</td>
        //         </tr>
        //     )
        // }
        console.log(res)
        return res;
    }

    render() {
        if (!this.state.tableData.length)
            return null;
        let res = [];
        this.state.tableData.map(message => (
            res.push(
                <tr key={message.message_uuid}>
                    <td>{message.from_who}</td>
                    <td>{message.phone}</td>
                    <td>{message.body}</td>
                    <td>{message.message_date_time}</td>
                    <td>{message.id}</td>
                    <td>
                        if {message.sent_status}{
                        <Badge color="success">Active</Badge>
                    }else{
                        <Badge color="danger">Failed</Badge>
                    }
                    </td>
                </tr>
            )
        ));
        return (
            <div className="animated fadeIn">
                <Row>
                    <Col>
                        <Card>
                            <CardHeader>
                                <i className="fa fa-align-justify"></i> List All messages
                            </CardHeader>
                            <CardBody>
                                <Table hover bordered striped responsive size="sm">
                                    <thead>
                                    <tr>
                                        <th>from</th>
                                        <th>to</th>
                                        <th>Message</th>
                                        <th>Message Date time</th>
                                        <th>Content</th>
                                        <th>Message Status</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    {res}
                                    </tbody>
                                </Table>
                                <nav>
                                    <Pagination>
                                        <PaginationItem><PaginationLink previous
                                                                        tag="button">Prev</PaginationLink></PaginationItem>
                                        <PaginationItem active>
                                            <PaginationLink tag="button">1</PaginationLink>
                                        </PaginationItem>
                                        <PaginationItem><PaginationLink tag="button">2</PaginationLink></PaginationItem>
                                        <PaginationItem><PaginationLink tag="button">3</PaginationLink></PaginationItem>
                                        <PaginationItem><PaginationLink tag="button">4</PaginationLink></PaginationItem>
                                        <PaginationItem><PaginationLink next
                                                                        tag="button">Next</PaginationLink></PaginationItem>
                                    </Pagination>
                                </nav>
                            </CardBody>
                        </Card>
                    </Col>
                </Row>
            </div>

        );
    }
}

export default Tables;
