/* (Beta) Export of data model OpenChannelFlowRegulation of the subject dataModel.OpenChannelManagement for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OpenChannelFlowRegulation_type AS ENUM ('OpenChannelFlowRegulation');
CREATE TABLE OpenChannelFlowRegulation (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasRegulationStructures json, hasStructuresSimulations json, id text, location json, name text, owner json, runBy text, seeAlso json, source text, type OpenChannelFlowRegulation_type);