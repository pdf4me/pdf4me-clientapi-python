import sys

sys.path.append('../../Pdf4mePythonClientApi')
sys.path.append('../../Pdf4mePythonClientApiTest')

import unittest
# from datetime import datetime

# from nose.tools import assert_raises, assert_equal, assert_not_equal

from pdf4me.client.pdf4me_client import Pdf4meClient
from pdf4me.client.job_client import JobClient
from pdf4me.helper.file_reader import FileReader
# from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.model import JobFlow, JobFlowPlan, ActionFlow, Pdf4meAction, ConvertToPdfAction, OptimizeAction, \
    StorageFolder, ExecutionTrigger, RunJobFlow, Document
from test_helper.check import Check
from test_helper.test_files import TestFiles
from pdf4me.helper.json_converter import JsonConverter


class JobClientTest(unittest.TestCase):
    pdf4me_client = Pdf4meClient()
    job_client = JobClient(pdf4me_client)

    test_files = TestFiles()
    check = Check()
    file_reader = FileReader()
    json_converter = JsonConverter()

    def test_save_job_flow(self):

        # request
        job_flow = JobFlow(
            # job_flow_id='548A29E3-B481-46B8-9DA7-50E1958495FF',
            name='TestJobFlow',
            active = True,
            action_flow=ActionFlow(
                name='TestJobFlow',
                actions=[
                    Pdf4meAction(
                        # action_id='',
                        action_type='convertToPdf',
                        action_config=self.json_converter.dump(
                            ConvertToPdfAction(
                                pdf_conformance='pdf17',
                                conversion_mode='fast',
                                action_id='00000000-0000-0000-0000-000000000000'
                            )
                        )
                    ),
                    Pdf4meAction(
                        # action_id='',
                        action_type='optimize',
                        action_config=self.json_converter.dump(
                            OptimizeAction(
                                profile='web',
                                use_profile=True,
                                action_id='00000000-0000-0000-0000-000000000000'
                            )
                        )
                    ),
                ]
            )
        )

        # res = self.job_client.save_job_flow(job_flow)

        # print(res)
        # validation
        # assert_not_equal(res['jobFlowId'], '00000000-0000-0000-0000-000000000000')

    def test_save_job_flow_plan(self):
        # request
        job_flow_plan = JobFlowPlan(
            job_flow_plan_id='C1CDACEC-D8FB-4D6C-9C00-F56C20888641',
            job_flow_id='548A29E3-B481-46B8-9DA7-50E1958495FF',
            machine_id='ABCDEFGHJIKL',
            enabled=False,
            active=True,
            source_folder=StorageFolder(
                storage_type="localSystem",
                folder_name="c:\\temp1",
                host="varun's pc"
            ),
            target_folder=StorageFolder(
                storage_type="localSystem",
                folder_name="c:\\temp",
                host="varun's pc"
            ),
            execution_trigger=ExecutionTrigger(
                # start_time=datetime(
                #     year=2020,
                #     month=7,
                #     day=9,
                #     hour=17,
                #     minute=3,
                #     second=30
                # ),
                cron_trigger='',
                continues=False
            )
        )

        # res = self.job_client.save_job_flow_plan(job_flow_plan)
        #
        # print(res)

        # validation
        # assert_not_equal(res['jobFlowPlanId'], '00000000-0000-0000-0000-000000000000')

    def test_run_job_flow(self):
        # request

        run_job_flow_req = RunJobFlow(
            action_flow=ActionFlow(
                name='TestJobFlow',
                actions=[
                    Pdf4meAction(
                        action_type='convertToPdf',
                        action_config=self.json_converter.dump(
                            ConvertToPdfAction(
                                pdf_conformance='pdf17',
                                conversion_mode='fast',
                                action_id='00000000-0000-0000-0000-000000000000'
                            )
                        )
                    ),
                    Pdf4meAction(
                        action_type='optimize',
                        action_config=self.json_converter.dump(
                            OptimizeAction(
                                profile='web',
                                use_profile=True,
                                action_id='00000000-0000-0000-0000-000000000000'
                            )
                        )
                    ),
                ]
            ),
            documents=[
                Document(
                    doc_data=self.test_files.text_data,
                    name=self.test_files.text_name
                ),
            ],
        )

        # res = self.job_client.run_job_flow(run_job_flow_req)
        #
        # print(res)

        # # validation
        # assert_not_equal(res['jobId'])
