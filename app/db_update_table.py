import sqlite3
conn = sqlite3.connect('testDB.db')


c = conn.cursor()

#add new release

c.execute("ALTER TABLE tutorial_model DROP COLUMN 'created_date';")

#'ansible' INTEGER(1), 'docker' INTEGER(1), 'kubernetes' INTEGER(1), 'rancher' NUMBER, 'jenkins' INTEGER(1), 'aws' INTEGER(1), 'github' INTEGER(1);")

#'python' INTEGER(1), 
#'linux' INTEGER(1), 
conn.commit()
#'id','ReleaseType','ReleaseVersion','DbResourcesRequired','ShortDescription','ImplementationStartDate','ImplementationEndDate','Description','Justification','ImplementationPlan','TestPlan','BackoutPlan','RiskAndImpactAnalysis','SparkStatus','SparkNumber','JIRAStatus','JIRANumber'
#INSERT INTO 'ReleaseTest' (`id`,`ReleaseType`,`ReleaseVersion`,`DbResourcesRequired`,`ShortDescription`,`ImplementationStartDate`,`ImplementationEndDate`,`Description`,`Justification`,`ImplementationPlan`,`TestPlan`,`BackoutPlan`,`RiskAndImpactAnalysis`,`SparkStatus`,`SparkNumber`,`JIRAStatus`,`JIRANumber`) 
 