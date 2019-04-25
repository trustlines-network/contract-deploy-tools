pragma solidity ^0.4.25;

import './subfolder/OtherContract.sol';

contract TestContract {

    int public state;

    constructor(int val) public {
        state = val;
    }

    function set(int a) public {
        state = a;
    }

    function testFunction(int a) public view returns (int) {
        return a + state;
    }

}
