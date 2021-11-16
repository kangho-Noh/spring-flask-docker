package com.example.docker.controller;

import com.example.docker.domain.Member;
import com.example.docker.repository.MemberRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class DataController {

    private MemberRepository memberRepository = MemberRepository.getInstance();

    @PostMapping("/data/save")
    public void addMember(@RequestBody Member member){
        System.out.println("[POST request Received : /data/save]");
        memberRepository.save(member);
    }

    @GetMapping("/members")
    public List<Member> listMembers(){
        System.out.println("[GET request Received : /members]");
        List<Member> all = memberRepository.findAll();
        return all;
    }
}
