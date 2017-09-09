import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { createStore } from 'redux'
import { Provider, connect } from 'react-redux'

class Counter extends Component {
    
    render() {
        const { value, onIncClick } = this.props;
        return (
            <div>
                <span>{value}</span>
                <button onClick={onIncClick}>inc</button>
            </div>
        )
    }
}

function mapStateToProps(state) {
    return {
        value: state.count
    }
}

function mapDispatchToProps(dispatch) {
    return {
        onIncClick: () => dispatch(increaseAction)
    }
}

const increaseAction = { type: 'increase' }

const App = connect(
    mapStateToProps,
    mapDispatchToProps,
)(Counter)

//Reducer
function counter(state = { count:0 }, action){
    const count = state.count
    switch(action.type){
        case 'increase':
            return { count: count + 1}
        default:
            return state
    }
}

const store = createStore(counter)

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
)