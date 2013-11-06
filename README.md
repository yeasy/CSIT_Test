CSIT Test
=========
*CSIT test tool for OpenDaylight Project*

* Version: 0.3
* Authors: [Baohua Yang](mailto:yangbaohua@gmail.com), [Denghui Huang](mailto:huangdenghui@gmail.com)
* Homepage: <https://github.com/yeasy/CSIT_Test>

##Get Code

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

* Start 2-layer tree topology network. For example, in Mininet, run  `sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2`
* Download the test tool code and run `python run.py`. There will be no failure report if all test cases are passed.

```
#Test case: switch manager
#Test case: topology manager
#Test case: forwarding rule manager
#Test case: statistics manager
#Test case: arp handler
#Test case: forwarding manager
#Test case: container manager

Process finished with exit code 0
```

* By default, all modules will be tested. If you want to test specific modules, please change the `module_to_test` variable in `run.py`.


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
* Integration into the robot framework.
* Interaction with other components, such as the network.

##About OpenDaylight
OpenDaylight is the first production-quality open-source SDN management platform sponsored by Linux Foundation. 
Lead SDN enterprises (Ericsson, IBM, Microsoft, Redhat, Cisco, Juniper, NEC, VMWare etc.) are involved to develop and support the project.
Please go to the official [homepage](http://www.opendaylight.org) page to find more information.

##About CSIT
See [CSIT](https://wiki.opendaylight.org/view/CrossProject:Integration_Group:CSIT) description page.
