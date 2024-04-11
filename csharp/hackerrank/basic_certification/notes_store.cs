using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution 
{
    public class NotesStore 
    {
        // Dictionary to store notes with their states as keys
        private Dictionary<string, List<string>> notes = new Dictionary<string, List<string>>();
        
        // Array of valid states
        private readonly string[] validStates = {"active", "completed", "others"};

        public NotesStore() {}

        // Method to add a note with a given state and name
        public void AddNote(string state, string name) 
        {
            // Check if the state is valid
            if (!IsValidState(state))
                throw new Exception($"Invalid state {state}");

            // Check if the name is not empty
            if (string.IsNullOrEmpty(name))
                throw new Exception("Name cannot be empty");

            // If the state does not exist in the dictionary, add it
            if (!notes.ContainsKey(state))
                notes[state] = new List<string>();

            // Add the note to the list of notes for the given state
            notes[state].Add(name);
        }

        // Method to get notes with a given state
        public List<string> GetNotes(string state) 
        {
            // Check if the state is valid
            if (!IsValidState(state))
                throw new Exception($"Invalid state {state}");

            // If the state does not exist in the dictionary, return an empty list
            if (!notes.ContainsKey(state))
                return new List<string>();

            // Return the list of notes for the given state
            return notes[state];
        }

        // Method to check if a state is valid
        private bool IsValidState(string state) 
        {
            return validStates.Contains(state);
        }
    }

    public class Solution 
    {
        public static void Main() 
        {
            // Create a NotesStore object
            var notesStoreObj = new NotesStore();
            
            // Read the number of operations
            var n = int.Parse(Console.ReadLine());

            for (var i = 0; i < n; i++) 
            {
                // Read the operation info
                var operationInfo = Console.ReadLine().Split(' ');

                try 
                {
                    // Perform the operation based on the operation info
                    if (operationInfo[0] == "AddNote")
                        notesStoreObj.AddNote(operationInfo[1], operationInfo.Length == 2 ? "" : operationInfo[2]);
                    else if (operationInfo[0] == "GetNotes") 
                    {
                        var result = notesStoreObj.GetNotes(operationInfo[1]);
                        if (result.Count == 0)
                            Console.WriteLine("No Notes");
                        else
                            Console.WriteLine(string.Join(",", result));
                    }
                    else 
                    {
                        Console.WriteLine("Invalid Parameter");
                    }
                }
                catch (Exception e) 
                {
                    Console.WriteLine("Error: " + e.Message);
                }
            }
        }
    }
}