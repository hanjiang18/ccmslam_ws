/*
 * @Author: hanjiang18 1763983820@qq.com
 * @Date: 2023-03-13 01:50:05
 * @LastEditors: hanjiang18 1763983820@qq.com
 * @LastEditTime: 2023-06-13 03:13:18
 * @FilePath: /ccmslam_ws/src/ccm_slam-master/cslam/src/server/ServerNode.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
/**
* This file is part of CCM-SLAM.
*
* Copyright (C): Patrik Schmuck <pschmuck at ethz dot ch> (ETH Zurich)
* For more information see <https://github.com/patriksc/CCM-SLAM>
*
* CCM-SLAM is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* CCM-SLAM is based in the monocular version of ORB-SLAM2 by Raúl Mur-Artal.
* CCM-SLAM partially re-uses modules of ORB-SLAM2 in modified or unmodified condition.
* For more information see <https://github.com/raulmur/ORB_SLAM2>.
*
* CCM-SLAM is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with CCM-SLAM. If not, see <http://www.gnu.org/licenses/>.
*/


#include <cslam/server/ServerSystem.h>

int main(int argc, char **argv) {

    ros::init(argc, argv, "CSLAM server node");
    for(int i = 0; i <argc; i++) {
        cout<<argv[i]<<endl;
    }
    if(argc != 2)
    {
        cerr << endl << "Usage: rosrun cslam clientnode path_to_vocabulary" << endl;
        ros::shutdown();
        return 1;
    }

    ros::NodeHandle Nh;
    ros::NodeHandle NhPrivate("~");

    boost::shared_ptr<cslam::ServerSystem> pSSys{new cslam::ServerSystem(Nh,NhPrivate,argv[1])};
   
    // pSSys->strname=argv[2];
    pSSys->InitializeClients();


    ROS_INFO("started CSLAM server node...");

    ros::MultiThreadedSpinner MSpin(2);

    MSpin.spin();
    pSSys->save();

    ros::waitForShutdown();

    return 0;
}
