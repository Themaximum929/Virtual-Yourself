def main():
    if args.webcam is not None:
        video_src = args.webcam
    else:
        video_src = args.video

    if video_src is None:
        print("No video source assigned, default video source would be used.")
        video_src = 0

    cap = cv2.VideoCapture(video_src)
    if video_src == 0:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        ret, first_frame = cap.read()

    mark_detec = LandmarkDetection()

    img_queue = Queue()
    box_queue = Queue()
    image_queue.put(first_frame)
    box_process = Process(target = get_face,
                          args=(mark_detec, img_queue, box_queue,))
    box_process.start()

    height, width = first_frame.shape[:2]
    post_esti = PostEstimation(img_size = (height, width))

    time = cv2.TickMeter()

    while True:
        ret, frame = cap.read()
        if ret is False:
            break
        if video_src == 0:
            frame = cv2.flip(frame, 2)

        img_queue.put(frame)

        facebox = box_queue.get()

        face_img = frame[facebox[1]: facebox[3], facebox[0]: facebox[2]]
        face_img = cv2.resize(face_img, (128, 128))
        facce_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

        time.start()
#need to add back function in landmark detection
        mark = landmark_detection.detect_marks(face_img)
        time.stop()

        marks *= (facebox[2] - facebox[0])
        marks[:, 0] += facebox[0]
        marks[:, 1] += facebox[1]

#need to add back function in pose estimator
        pose = pose_estimator.solve_pose_by_68_points(marks)

 # Stabilize the pose.
        steady_pose = []
        pose_np = np.array(pose).flatten()
        for value, ps_stb in zip(pose_np, pose_stabilizers):
            ps_stb.update([value])
            steady_pose.append(ps_stb.state[0])
        steady_pose = np.reshape(steady_pose, (-1, 3))

        pose_estimator.draw_annotation_box(
            frame, steady_pose[0], steady_pose[1], color=(128, 255, 128))

        cv2.imshow("Preview", frame)
        if cv2.waitKey(10) == 27:
            break

    # Clean up the multiprocessing process.
    box_process.terminate()
    box_process.join()




if _name_ == "_main_":
    main()
