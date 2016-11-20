# polldaddyvoter
A votebot for polldaddy polls.

###Setup
For an embedded poll, the poll address can be found in the html (inspect element or whathaveyou).
Once on the polldaddy page, all ids are avaliable in HTML.

Set `poll_id` value equal to the pollid. This should be in the url, among other places.

Then create an array of `voteOption` objects for each thing that should be voted for.

`choices= [voteOption(option_id, name_string, times_to_vote)), ...]`

`option_id` can also be found in the page html.
The `name_string` is only for identification purposes in console output and has no effect on the functioning of the program.
`times_to_vote` can be used to setup a ratio between different voting options and will simply vote for the specific choice the specified number of times before moving to the next.

Highly recommend using this with AWS scaling groups or similar solution to increase votes/second. This bot only works on polls that allow voting multiple times, but will still be locked out after a number of attempts for some interval.

