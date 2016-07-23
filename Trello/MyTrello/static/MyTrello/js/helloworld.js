/**
 * This file provided by Facebook is for non-commercial testing and evaluation
 * purposes only. Facebook reserves all rights not expressly granted.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * FACEBOOK BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

var Board = React.createClass({
  render: function() {

    //console.log(this.props.board_name);
    return (
      <div className="board">
        <h2 className="boardName">
          {this.props.board_name}
        </h2>
      </div>
    );
  }
});

var BoardBox = React.createClass({
  loadBoardsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  handleBoardSubmit: function(board) {
    var boards = this.state.data;

    //console.log("#########");
    // Optimistically set an id on the new board. It will be replaced by an
    // id generated by the server. In a production application you would likely
    // not use Date.now() for this and would have a more robust system in place.
    board.id = Date.now();
    var newBoards = boards.concat([board]);
    this.setState({data: newBoards});
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: board,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        this.setState({data: boards});
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadBoardsFromServer();
    setInterval(this.loadBoardsFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <div className="boardBox">
        <h1>My Boards:</h1>
        <BoardList data={this.state.data} />
        <BoardForm onBoardSubmit={this.handleBoardSubmit} />
      </div>
    );
  }
});

var BoardList = React.createClass({
  render: function() {

    //console.log(this.props.data);

    var boardNodes = this.props.data.map(function(board) {
      return (
        <Board board_name={board.board_name} key={board.id}>
        </Board>
      );
    });
    return (
      <div className="boardList">
        {boardNodes}
      </div>
    );
  }
});

var BoardForm = React.createClass({
  getInitialState: function() {
    return {board_name: ''};
  },
  handleBoardNameChange: function(e) {
    this.setState({board_name: e.target.value});
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var board_name = this.state.board_name.trim();
    if (!board_name) {
      return;
    }
    this.props.onBoardSubmit({board_name: board_name, csrfmiddlewaretoken: csrftoken});
    this.setState({board_name: ''});
  },
  render: function() {
    return (
      <form className="boardForm" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Board Name.."
          value={this.state.board_name}
          onChange={this.handleBoardNameChange}
        />
        <input type="submit" value="Post" />
      </form>
    );
  }
});

ReactDOM.render(
  <BoardBox url="records/" pollInterval={2000} />,
  document.getElementById('content')
);
