# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified
One edge case I have identified is when there could be zero students, or many students with zero 
marks. 

I also ensured that students that were submitted are not blank. They are allowed to have no mark, as mentioned in the spec, but if they submit a null object, it fails. 
2) How you have accounted for this in your implementation
I handled this by counting the number of students that actually have marks. If the number of students with marks is zero, then I return a JSON object with default, zero values.

I accounted for the second one by having checks in place for a blank object, and for an object with missing fields. 