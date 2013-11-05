CSIT Test
=========
*CSIT test tool for OpenDaylight Project*

* Version: 0.2
* Authors: [Baohua Yang](mailto:yangbaohua@gmail.com), [Denghui Huang](mailto:huangdenghui@gmail.com)
* Homepage: <https://github.com/yeasy/CSIT_Test>

##Get Code
`git clone git@github.com:yeasy/CSIT_Test.git`

or

`git clone https://github.com/yeasy/CSIT_Test.git`

##Usage
###Prerequisites
* Python 2.6/2.7
* Python [Requests library](http://www.python-requests.org)

  ` pip install requests`

* [OpenDaylight Controller](https://wiki.opendaylight.org/view/GettingStarted:Developer_Main)
   * Download and build OpenDaylight Controller

   ```
   git clone https://git.opendaylight.org/gerrit/p/controller.git
   cd controller/opendaylight/distribution/opendaylight
   mvn clean install -DskipTests -Dmaven.compile.fork=true -U
   ```
* [Mininet](http://mininet.org/walkthrough/)

###Run Test
* Start the [OpenDaylight Controller](https://wiki.opendaylight.org/view/GettingStarted:Developer_Main)

 ```
  cd controller/target/distribution.opendaylight-0.1.0-SNAPSHOT-osgipackage/opendaylight/
  ./run.sh
  ```

* Start 2-layer tree topology network, in Mininet, run  `sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2`
* Configure gateway in the controller web GUI, name = `gateway`, subnet = `10.0.0.254/24`
* In Mininet, run `h1 ping h2` to make sure the network is connected.
* Download the test tool code and run `python run.py`. There will be no failure report if all test cases are passed.

##Code Description
###`base/`
The test code for the OpenDaylight base edition.
* `run.py`
Main runnable script to start the test.
* `restlib.py`
Library for the restful actions, e.g., `GET`, `PUT`, `POST`, `DELETE`, based on the python requests lib.
* `testmodule.py`
Basic class of a module to be tested.
* `cases/`
Store the test cases for all modules. Test case is named as the module name, e.g., switch_manager.py is the test case for the switch manager module.

##Development Plan
* Finish all module test in OpenDaylight's base release.
* Integrated into the robot framework.

##About OpenDaylight
OpenDaylight is the first production-quality open-source SDN management platform sponsored by Linux Foundation. 
Lead SDN enterprises (Ericsson, IBM, Microsoft, Redhat, Cisco, Juniper, NEC, VMWare etc.) are involved to develop and support the project.
Please go to the official [homepage](http://www.opendaylight.org) page to find more information.

##About CSIT
See [CSIT](https://wiki.opendaylight.org/view/CrossProject:Integration_Group:CSIT) description page.
