Dynamic programming is not about taking the max over something, it's instead about
recursiving over the choices.

List all the choices you can make at this point and the rewards associated with each choice
Note that the rewards probably involve the results from other subproblems.

Then compute the max over the choices
Then save that max in memory (memo)
