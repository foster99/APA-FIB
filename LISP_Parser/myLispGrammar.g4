

grammar myLispGrammar; //

// tokens
WORD:       [A-Za-z-]+;
NUMBER:     [0-9]+;


root : instance* EOF;

instance: '(' def_instance uni_name items_list+ ')';

items_list: '(' column_name (value | typed_value) ')';


value_type: ratio_
          | thous
          | money
          | scale;

value:  ratio
      | interval
      | WORD
      | NUMBER;

typed_value:  value_type value;

// values
ratio:      NUMBER ':' NUMBER;
interval:   dual | single;

// interval type
single:     NUMBER '-';
dual:       NUMBER '-' NUMBER;


column_name:  this_state
            | location
            | control
            | num_students
            | gender
            | num_students
            | student_faculty
            | sat_verbal
            | sat_maths
            | expenses
            | finantial_aid
            | number_appli
            | perc_admitance
            | perc_enrolled
            | academics
            | social_scale
            | quality_of_life
            | academic_emphasis
            ;

// INSTANCES
def_instance:     'DEF-INSTANCE'|'def-instance';
uni_name:         WORD;

// TYPES
ratio_:           'RATIO:'|'ratio:';
thous:            'THOUS:'|'thous:';
money:            'THOUS$:'|'thous$:';
scale:            'SCALE:'|'scale:';

// COLUMN NAMES
this_state:       'STATE'|'state';
location:         'LOCATION'|'location';
control:          'CONTROL'|'control';
num_students:     'NO-OF-STUDENTS'|'no-of-students';
gender:           'MALE:FEMALE'|'male:female';
student_faculty:  'STUDENT:FACULTY'|'student:faculty';
sat_verbal:       'SAT VERBAL'|'sat verbal';
sat_maths:         'SAT MATH'|'sat math';
expenses:         'EXPENSES'|'expenses';
finantial_aid:    'PERCENT-FINANCIAL-AID'|'percent-financial-aid';
number_appli:     'NO-APPLICANTS'|'no-applicants';
perc_admitance:   'PERCENT-ADMITTANCE'|'percent-admittance';
perc_enrolled:    'PERCENT-ENROLLED'|'percent-enrolled';
academics:        'ACADEMICS'|'academics';
social_scale:     'SOCIAL'|'social';
quality_of_life:  'QUALITY-OF-LIFE'|'quality-of-life';
academic_emphasis:'ACADEMIC-EMPHASIS'|'academic-emphasis';

WS:         [ \t\r\n]+ -> skip;
