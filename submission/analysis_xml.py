"""
This class will generate Analysis XML that could be send to ENA
"""

from lxml import etree


class AnalysisXML:
    def __init__(self, alias, centre_name, sample_accession, run_accession,
                 study_accession, pipeline_name, pipeline_version,
                 analysis_date, analysis_files, title, description,
                 analysis_xml_file):
        self.alias = alias
        self.centre_name = centre_name
        self.sample_accession = sample_accession
        self.run_accession = run_accession
        self.study_accession = study_accession
        self.pipeline_name = pipeline_name
        self.pipeline_version = pipeline_version
        self.analysis_date = analysis_date
        self.analysis_files = analysis_files
        self.title = title
        self.description = description
        self.analysis_xml_file = analysis_xml_file

    def build_xml(self):
        analysis_set = etree.Element('ANALYSIS_SET')
        analysis_xml = etree.ElementTree(analysis_set)
        analysis_elt = etree.SubElement(analysis_set, 'ANALYSIS',
                                        alias=self.alias,
                                        center_name=self.centre_name,
                                        analysis_date=self.analysis_date)
        title = etree.SubElement(analysis_elt, 'TITLE')
        title.text = self.title
        description = etree.SubElement(analysis_elt, 'DESCRIPTION')
        description.text = self.description
        etree.SubElement(analysis_elt, 'STUDY_REF',
                         accession=self.study_accession)
        etree.SubElement(analysis_elt, 'SAMPLE_REF',
                         accession=self.sample_accession)
        etree.SubElement(analysis_elt, 'RUN_REF',
                         accession=self.run_accession)
        analysis_type = etree.SubElement(analysis_elt, 'ANALYSIS_TYPE')
        etree.SubElement(analysis_type, 'PATHOGEN_ANALYSIS')
        files = etree.SubElement(analysis_elt, 'FILES')
        etree.SubElement(files, 'FILE',
                         filename=self.analysis_files[0].file_name,
                         filetype=self.analysis_files[0].file_type,
                         checksum_method="MD5",
                         checksum=self.analysis_files[0].file_md5)
        etree.SubElement(files, 'FILE',
                         filename=self.analysis_files[1].file_name,
                         filetype=self.analysis_files[1].file_type,
                         checksum_method="MD5",
                         checksum=self.analysis_files[1].file_md5)

        # Analysis attributes
        analysis_attributes = etree.SubElement(analysis_elt,
                                               'ANALYSIS_ATTRIBUTES')

        analysis_attribute = etree.SubElement(analysis_attributes,
                                              'ANALYSIS_ATTRIBUTE')

        etree.SubElement(analysis_attribute, "TAG").text = "PIPELINE_NAME"
        etree.SubElement(analysis_attribute, "VALUE").text = self.pipeline_name

        analysis_attribute = etree.SubElement(analysis_attributes,
                                              'ANALYSIS_ATTRIBUTE')
        etree.SubElement(analysis_attribute, "TAG").text = "PIPELINE_VERSION"
        etree.SubElement(analysis_attribute,
                         "VALUE").text = self.pipeline_version
        # Writing xml file
        analysis_xml.write(self.analysis_xml_file, pretty_print=True,
                           xml_declaration=True, encoding='UTF-8')
