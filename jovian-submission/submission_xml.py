"""
This class will generate Submission XML that could be send to ENA
"""

from lxml import etree


class SubmissionXML:
    def __init__(self, alias, submission_centre, action, submission_xml_file,
                 source_xml, schema):
        self.alias = alias
        self.submission_centre = submission_centre
        self.action = action
        self.submission_xml_file = submission_xml_file
        self.source_xml = source_xml
        self.schema = schema

    def build_xml(self):
        submission_set = etree.Element('SUBMISSION_SET')
        submission_xml = etree.ElementTree(submission_set)
        submission_elt = etree.SubElement(submission_set, 'SUBMISSION',
                                          alias=self.alias,
                                          center_name=self.submission_centre)
        actions_elt = etree.SubElement(submission_elt, 'ACTIONS')
        action_elt = etree.SubElement(actions_elt, 'ACTION')
        etree.SubElement(action_elt, self.action, source=self.source_xml,
                         schema=self.schema)
        submission_xml.write(self.submission_xml_file, pretty_print=True,
                             xml_declaration=True, encoding='UTF-8')
