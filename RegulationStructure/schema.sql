/* (Beta) Export of data model RegulationStructure of the subject dataModel.OpenChannelManagement for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE RegulationStructure_type AS ENUM ('RegulationStructure');
CREATE TABLE RegulationStructure (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, numberOfGates NUMERIC, numberOfSpillways NUMERIC, owner JSON, position JSON, source TEXT, tag TEXT, teleCommand BOOLEAN, type RegulationStructure_type);