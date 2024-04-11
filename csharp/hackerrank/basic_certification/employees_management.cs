using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution
{
    public class Solution
    {
        // This method calculates the average age for each company
        public static Dictionary<string, int> AverageAgeForEachCompany(List<Employee> employees)
        {
            // Group employees by company, select the company and ages, order by company, and convert to dictionary
            return employees.GroupBy(employee => employee.Company)
                .Select(group => new { Company = group.Key, Ages = group.Select(employee => employee.Age )})
                .OrderBy(obj => obj.Company)
                .ToDictionary(obj => obj.Company, obj => (int)Math.Round(obj.Ages.Average()));
        }
        
        // This method counts the number of employees for each company
        public static Dictionary<string, int> CountOfEmployeesForEachCompany(List<Employee> employees)
        {
            // Group employees by company, order by company, and convert to dictionary with count of employees
            return employees.GroupBy(employee => employee.Company)
                .OrderBy(group => group.Key)
                .ToDictionary(group => group.Key, group => group.Count());
        }
        
        // This method finds the oldest employee for each company
        public static Dictionary<string, Employee> OldestAgeForEachCompany(List<Employee> employees)
        {
            // Group employees by company, order by company, and convert to dictionary with oldest employee
            return employees.GroupBy(employee => employee.Company)
                .OrderBy(group => group.Key)
                .ToDictionary(group => group.Key, group => group.Where(emp => emp.Age == group.Max(employee => employee.Age)).First()); 
        }

        public static void Main()
        {
            // Read the number of employees
            int countOfEmployees = int.Parse(Console.ReadLine());

            var employees = new List<Employee>();

            // Read employee data
            for (int i = 0; i < countOfEmployees; i++)
            {
                string str = Console.ReadLine();
                string[] strArr = str.Split(' ');
                employees.Add(new Employee
                {
                    FirstName = strArr[0],
                    LastName = strArr[1],
                    Company = strArr[2],
                    Age = int.Parse(strArr[3])
                });
            }

            // Print the average age for each company
            foreach (var emp in AverageAgeForEachCompany(employees))
            {
                Console.WriteLine($"The average age for company {emp.Key} is {emp.Value}");
            }

            // Print the count of employees for each company
            foreach (var emp in CountOfEmployeesForEachCompany(employees))
            {
                Console.WriteLine($"The count of employees for company {emp.Key} is {emp.Value}");
            }

            // Print the oldest employee for each company
            foreach (var emp in OldestAgeForEachCompany(employees))
            {
                Console.WriteLine($"The oldest employee of company {emp.Key} is {emp.Value.FirstName} {emp.Value.LastName} having age {emp.Value.Age}");
            }
        }
    }

    // Employee class with properties for first name, last name, age, and company
    public class Employee
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public int Age { get; set; }
        public string Company { get; set; }
    }
}